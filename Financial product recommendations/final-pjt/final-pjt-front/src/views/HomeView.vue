<template>
  <div class="background-image">
    <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="@/assets/kivotos.png" class="d-block w-100" alt="First slide">
          <div class="carousel-caption d-flex justify-content-center align-items-center">
            <div class="carousel-textbox">
              <span>상품 소개</span>
            </div>
          </div>
        </div>
        <div class="carousel-item">
          <img src="@/assets/beach.jpg" class="d-block w-100" alt="Second slide">
          <div class="carousel-caption d-flex justify-content-center align-items-center">
            <div class="carousel-textbox">
              <span>환율 계산기</span>
            </div>
          </div>
        </div>
        <div class="carousel-item">
          <img src="@/assets/kivotos2.jpg" class="d-block w-100" alt="Third slide">
          <div class="carousel-caption d-flex justify-content-center align-items-center">
            <div class="carousel-textbox">
              <span>은행 찾기</span>
            </div>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
  <footer class="d-flex justify-content-center align-items-center">
      <img src="@/assets/coin.jpg" alt="money" width="400px" height="300px">
      <div class="footer-textbox ms-3">
        <span>&nbsp;연금과 저금만으로 미래를 대비하기에는 불안한 사회, 우리는 우리의 미래를 위해 더 많은 노력과 관심을 쏟아야 합니다. <br><br>
          &nbsp;하지만 직접 유용한 상품을 찾는 것은 많은 시간이 필요하며 정보의 확실성도 검증해야 되서 어떻게 미래를 대비해야 될지 걱정이 많이 되실겁니다. <br> <br>&nbsp; 그런 분들을 위해 저희 노후자금준비하조는 적은 시간과 노력으로 여러분의 미래를 대비할 최고의 상품을 찾아드립니다.</span>
      </div>
    </footer>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style scoped>
.background-image {
  width: 100vw;
  height: 50vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start; /* Align items to the top */
  align-items: center;
  font-family: 'BlueArchive', sans-serif;
}

.carousel {
  width: 100%; /* Full width of the viewport */
  height: 30vh; /* 30% of the viewport height */
}

.carousel-inner img {
  height: 50vh;
  object-fit: cover;
}

.carousel-caption {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.carousel-textbox {
  background: rgba(255, 255, 255, 0.5);
  color: grey;
  padding: 40px;
  border-radius: 10px;
  font-size: 30px;
}

.carousel-control-prev,
.carousel-control-next {
  height: 50vh;
}

footer {
  margin-top: 50px;
  margin-left: 500px;
  margin-right: 500px;
  font-family: 'BlueArchive', sans-serif;
  font-size: 18px;
  flex: 2;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

.footer-textbox {
  width: 500px;
  height: 300px;
}
</style>
