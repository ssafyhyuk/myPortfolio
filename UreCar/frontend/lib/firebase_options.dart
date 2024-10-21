// File generated by FlutterFire CLI.
// ignore_for_file: type=lint
import 'package:firebase_core/firebase_core.dart' show FirebaseOptions;
import 'package:flutter/foundation.dart'
    show defaultTargetPlatform, kIsWeb, TargetPlatform;

/// Default [FirebaseOptions] for use with your Firebase apps.
///
/// Example:
/// ```dart
/// import 'firebase_options.dart';
/// // ...
/// await Firebase.initializeApp(
///   options: DefaultFirebaseOptions.currentPlatform,
/// );
/// ```
class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    if (kIsWeb) {
      return web;
    }
    switch (defaultTargetPlatform) {
      case TargetPlatform.android:
        return android;
      case TargetPlatform.iOS:
        return ios;
      case TargetPlatform.macOS:
        return macos;
      case TargetPlatform.windows:
        return windows;
      case TargetPlatform.linux:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for linux - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      default:
        throw UnsupportedError(
          'DefaultFirebaseOptions are not supported for this platform.',
        );
    }
  }

  static const FirebaseOptions web = FirebaseOptions(
    apiKey: 'AIzaSyDmyIZ0rVYq-jdrHQer1QNUtryS69G6TIU',
    appId: '1:44688138191:web:5f761c08c4d042a248fcba',
    messagingSenderId: '44688138191',
    projectId: 'urecar-5c5e8',
    authDomain: 'urecar-5c5e8.firebaseapp.com',
    storageBucket: 'urecar-5c5e8.appspot.com',
    measurementId: 'G-7BGBHMPYXE',
  );

  static const FirebaseOptions android = FirebaseOptions(
    apiKey: 'AIzaSyDOaEQGwTfeAFLmIMfDzZVBCf5gk_OgNZ8',
    appId: '1:44688138191:android:63c58d3e82ee474948fcba',
    messagingSenderId: '44688138191',
    projectId: 'urecar-5c5e8',
    storageBucket: 'urecar-5c5e8.appspot.com',
  );

  static const FirebaseOptions ios = FirebaseOptions(
    apiKey: 'AIzaSyDuLtBIFobJ6cgaw5Y-VjQJ8G5a04gSP1Y',
    appId: '1:44688138191:ios:ae57f3d9a9b7753748fcba',
    messagingSenderId: '44688138191',
    projectId: 'urecar-5c5e8',
    storageBucket: 'urecar-5c5e8.appspot.com',
    iosBundleId: 'com.example.frontend',
  );

  static const FirebaseOptions macos = FirebaseOptions(
    apiKey: 'AIzaSyDuLtBIFobJ6cgaw5Y-VjQJ8G5a04gSP1Y',
    appId: '1:44688138191:ios:ae57f3d9a9b7753748fcba',
    messagingSenderId: '44688138191',
    projectId: 'urecar-5c5e8',
    storageBucket: 'urecar-5c5e8.appspot.com',
    iosBundleId: 'com.example.frontend',
  );

  static const FirebaseOptions windows = FirebaseOptions(
    apiKey: 'AIzaSyDmyIZ0rVYq-jdrHQer1QNUtryS69G6TIU',
    appId: '1:44688138191:web:920121e33642e40048fcba',
    messagingSenderId: '44688138191',
    projectId: 'urecar-5c5e8',
    authDomain: 'urecar-5c5e8.firebaseapp.com',
    storageBucket: 'urecar-5c5e8.appspot.com',
    measurementId: 'G-8V59Z6F3Z9',
  );
}
