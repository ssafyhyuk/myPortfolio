<template>
    <div class="center">
      <div class="com-box">
        <h1>게시판</h1>
        <div class="header">
          <router-link :to="{ name: 'createarticle' }" class="create-button">게시글 등록</router-link>
        </div>
        <div class="com-bar">
          <span class="com-num">번호</span>
          <span class="com-tit">제목</span>
          <span class="com-writer">작성자</span>
          <span class="com-date">작성일</span>
        </div>
        <ArticleList 
          v-for="article in store.articles"
          :key="article.id"
          :article="article"
        />
        <footer>
          <nav aria-label="Page navigation example">
            <ul class="pagination">
              <li class="page-item"><a class="page-link" href="#">Previous</a></li>
              <li class="page-item"><a class="page-link" href="#">1</a></li>
              <li class="page-item"><a class="page-link" href="#">2</a></li>
              <li class="page-item"><a class="page-link" href="#">3</a></li>
              <li class="page-item"><a class="page-link" href="#">Next</a></li>
            </ul>
          </nav>
        </footer>
      </div>
    </div>
  </template>
  
  <script setup>
  import ArticleList from '@/components/ArticleList.vue';
  import { useCounterStore } from '@/stores/counter';
  import { onMounted } from 'vue';
  import { RouterLink } from 'vue-router';
  
  const store = useCounterStore();
  
  onMounted(() => {
    store.getArticles();
  });
  </script>
  
  <style scoped>
  .center {
    display: flex;
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    height: 100vh; /* Full viewport height */
    background-image: url('@/assets/desk.jpg');
    background-size: cover;
    background-position: center;
    font-family: 'BlueArchive', sans-serif;
  }
  
  .com-box {
  background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white background */
  border-radius: 20px;
  padding: 20px;
  width: 1000px;
  height: 800px;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for a lifted effect */
  backdrop-filter: blur(10px); /* Blur background for better readability */
  box-sizing: border-box;
}
  
  .header {
    width: 100%;
    display: flex;
    justify-content: flex-end; /* Align to the right */
    margin-bottom: 10px; /* Add some space below the header */
  }
  
  .create-button {
    background-color: #2699E6;
    color: white;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s;
    font-family: 'BlueArchive';
    font-style: normal;
    font-weight: 700;
    font-size: 16px;
    line-height: 110%;
    cursor : pointer
  }
  
  .create-button:hover {
    background-color: #0056b3;
  }
  
  .com-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%; /* Full width of the .com-box */
    padding: 10px 0;
    border-top: 1px solid blue;
    border-bottom: 1px solid black;
  }
  
  .com-bar span {
    display: inline-block; /* Ensure span elements are treated as inline-block */
    text-align: center; /* Center align the text */
  }
  
  .com-num {
    width: 50px;
  }
  
  .com-tit {
    flex-grow: 1; /* Take up the remaining space */
    text-align: left; /* Align text to the left */
    margin-left: 10px; /* Add some margin to the left */
  }
  
  .com-writer {
    width: 180px;
  }
  
  .com-date {
    width: 150px;
  }
  
  .pagination {
    justify-content: center;
    margin-top: 20px;
  }
  
  .page-item .page-link {
    color: #007bff;
    margin: 0 5px;
  }
  
  footer {
    width: 100%; /* Ensure footer takes the full width of the com-box */
    display: flex;
    justify-content: center; /* Center pagination inside the footer */
  }
  
  </style>
  