import 'dart:convert';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:frontend/controller.dart';
import 'package:get/get.dart';
import 'package:http/http.dart' as http;
import 'package:dio/dio.dart' as dio_pkg;

class ApiService {
  final MainController controller = Get.put(MainController());
  String? baseUrl = dotenv.env['FLUTTER_APP_SERVER_URL'];

  Future<dynamic> signUp(Map<String, dynamic> formData) async {
    final url = Uri.parse('$baseUrl/members/signup');
    try {
      final response = await http.post(
        url,
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode(formData),
      );
      if (response.statusCode == 200) {
        return response.statusCode;
      } else {
        final responseData = jsonDecode(response.body);
        return responseData;
      }
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> emailCheck(Map<String, dynamic> formData) async {
    final url = Uri.parse('$baseUrl/members/emailCheck');
    try {
      final response = await http.post(
        url,
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode(formData),
      );
      if (response.statusCode == 200) {
        if (response.body == "true") {
          return true;
        } else {
          return false;
        }
      } else {
        final responseData = jsonDecode(response.body);
        return responseData;
      }
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> login(Map<String, dynamic> formData) async {
    const storage = FlutterSecureStorage();
    final url = Uri.parse('$baseUrl/login');
    try {
      final response = await http.post(
        url,
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode(formData),
      );
      if (response.statusCode == 200) {
        final responseData = jsonDecode(response.body);
        controller.memberEmail.value = formData['email'];
        controller.accessToken.value = responseData['accessToken'];
        controller.memberId.value = responseData['memberId'];
        controller.memberName.value = responseData['memberName'];
        controller.memberRole.value = responseData['memberRole'];
        await storage.write(
            key: "login",
            value:
                "${controller.memberEmail.value} ${controller.accessToken.value} ${controller.memberId.value} ${controller.memberName.value} ${controller.memberRole.value}");
        await sendFCMToken();

        return response.statusCode;
      } else {
        final responseData = jsonDecode(response.body);
        return responseData;
      }
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> sendFCMToken() async {
    final url = Uri.parse('$baseUrl/members/token');
    if (controller.memberId.value == 0 || controller.fcmToken.value == "") {
      return 0;
    }
    final formData = {
      "memberId": controller.memberId.value,
      "token": controller.fcmToken.value
    };
    try {
      final response = await http.post(url,
          headers: {
            'Content-Type': 'application/json',
          },
          body: jsonEncode(formData));
      if (response.statusCode == 200) {
        return 200;
      } else {
        final responseData = jsonDecode(response.body);
        return responseData;
      }
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> withdraw(Map<String, dynamic> formData) async {
    final url = Uri.parse('$baseUrl/members');
    try {
      final response = await http.delete(
        url,
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode(formData),
      );
      if (response.statusCode == 200) {
        controller.accessToken.value = "";
        controller.memberId.value = 0;
        controller.memberName.value = "";

        return response.statusCode;
      } else {
        final responseData = jsonDecode(response.body);
        return responseData;
      }
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> createReport(
      Map<String, dynamic> formData, String imagePath) async {
    dio_pkg.Dio dio = dio_pkg.Dio();
    final url = '$baseUrl/reports';
    try {
      dio_pkg.FormData formDataWithFile = dio_pkg.FormData.fromMap({
        'dto': dio_pkg.MultipartFile.fromString(
          jsonEncode(formData['dto']),
          contentType: dio_pkg.DioMediaType.parse('application/json'),
        ),
        'file': await dio_pkg.MultipartFile.fromFile(imagePath)
      });
      dio_pkg.Response response = await dio.post(
        url,
        data: formDataWithFile,
        options: dio_pkg.Options(
          validateStatus: (status) => true,
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        ),
      );
      final responseData = response.data;

      return responseData;
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> sendSecondImage(
      Map<String, dynamic> formData, String imagePath) async {
    dio_pkg.Dio dio = dio_pkg.Dio();
    final url = '$baseUrl/reports/secondImage';

    try {
      dio_pkg.FormData formDataWithFile = dio_pkg.FormData.fromMap({
        'dto': dio_pkg.MultipartFile.fromString(
          jsonEncode(formData['dto']),
          contentType: dio_pkg.DioMediaType.parse('application/json'),
        ),
        'file': await dio_pkg.MultipartFile.fromFile(imagePath)
      });
      dio_pkg.Response response = await dio.post(
        url,
        data: formDataWithFile,
        options: dio_pkg.Options(
          validateStatus: (status) => true,
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        ),
      );

      final responseData = response.data;

      return responseData;
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> findReports(String memberId, String startDate, String endDate,
      String? processStatus) async {
    final queryParameters = {
      'memberId': memberId,
      'startDate': startDate,
      'endDate': endDate,
    };

    if (processStatus != null) {
      queryParameters['processStatus'] = processStatus;
    }

    final uri =
        Uri.parse('$baseUrl/reports').replace(queryParameters: queryParameters);

    try {
      final response = await http.get(
        uri,
        headers: {
          'Content-Type': 'application/json',
        },
      );

      if (response.statusCode == 200) {
        final List<dynamic> responseData =
            jsonDecode(utf8.decode(response.bodyBytes));
        return responseData;
      } else {
        return [];
      }
    } catch (e) {
      return [];
    }
  }

  Future<dynamic> findGallery() async {
    final url = Uri.parse('$baseUrl/reports/gallery');
    final formData = {"memberId": controller.memberId.value};
    try {
      final response = await http.post(url,
          headers: {'Content-Type': 'application/json'},
          body: jsonEncode(formData));
      if (response.statusCode == 200) {
        final Map<String, dynamic> responseData = jsonDecode(response.body);
        return responseData;
      } else {
        final Map<String, dynamic> errorData = jsonDecode(response.body);
        return errorData;
      }
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> updateMember(Map<String, dynamic> formData) async {
    final url = Uri.parse('$baseUrl/members');
    try {
      final response = await http.put(
        url,
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode(formData),
      );
      if (response.statusCode == 200) {
        return response.statusCode;
      } else {
        final responseData = jsonDecode(response.body);
        return responseData;
      }
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> findSpecificReport(String id) async {
    final url = Uri.parse('$baseUrl/reports/detail/$id');

    try {
      final response =
          await http.get(url, headers: {'Content-Type': 'application/json'});
      if (response.statusCode == 200) {
        final responseData = jsonDecode(utf8.decode(response.bodyBytes));
        return responseData;
      } else {
        return {
          'error': 'Failed to fetch report',
          'status': response.statusCode
        };
      }
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> findOfficialReport() async {
    final url = Uri.parse('$baseUrl/officials');

    try {
      final response =
          await http.get(url, headers: {'Content-Type': 'application/json'});
      if (response.statusCode == 200) {
        final responseData = jsonDecode(utf8.decode(response.bodyBytes));
        return responseData;
      } else {
        return {
          'error': 'Failed to fetch report',
          'status': response.statusCode
        };
      }
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> findSpecificOfficialReport(String id) async {
    final url = Uri.parse('$baseUrl/officials/reports/$id');

    try {
      final response =
          await http.get(url, headers: {'Content-Type': 'application/json'});
      if (response.statusCode == 200) {
        final responseData = jsonDecode(utf8.decode(response.bodyBytes));
        return responseData;
      } else {
        return {
          'error': 'Failed to fetch report',
          'status': response.statusCode
        };
      }
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> acceptReport(Map<String, dynamic> formData) async {
    final url = Uri.parse('$baseUrl/officials');

    try {
      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode(formData),
      );
      if (response.statusCode == 200) {
        final responseData = jsonDecode(response.body);
        return responseData;
      } else {
        return {
          'error': 'Failed to fetch report',
          'status': response.statusCode
        };
      }
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> findNotifications() async {
    final int memberId = controller.memberId.value;
    final url = Uri.parse('$baseUrl//notifications/$memberId');

    try {
      final response =
          await http.get(url, headers: {'Content-Type': 'application/json'});

      final responseData = jsonDecode(utf8.decode(response.bodyBytes));
      return responseData;
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> removeNotification(int notificationsId) async {
    final url = Uri.parse('$baseUrl//notifications/$notificationsId');

    try {
      final response =
          await http.delete(url, headers: {'Content-Type': 'application/json'});

      final responseData = response.body;
      return responseData;
    } catch (e) {
      return e;
    }
  }

  Future<dynamic> removeAllNotifications() async {
    final int memberId = controller.memberId.value;
    final url = Uri.parse('$baseUrl//notifications/all/$memberId');

    try {
      final response =
          await http.delete(url, headers: {'Content-Type': 'application/json'});

      final responseData = response.body;
      return responseData;
    } catch (e) {
      return e;
    }
  }
}
