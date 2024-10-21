<template>
    
    <div class="com-bar-item">
        <span class="com-num">{{ article.id }}</span>
        <span class="com-tit">
            <RouterLink :to="{ name: 'articledetail', params: { id: article.id } }" class ="none">{{ article.title }}</RouterLink>
        </span>
        <span class="com-writer">{{ article.nickname }}</span>
        <span class="com-date">{{ article.created_at.slice(0, 10) }}</span>
    </div>
</template>

<script setup>
defineProps({
    article: Object
})
</script>

<style scoped>
.com-bar-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding: 10px 0;
    border-bottom: 1px solid #ccc;
}
.com-bar-item .com-num {
    width: 50px;
    text-align: center;
}
.com-bar-item .com-tit {
    flex-grow: 1;
    margin-left: 10px;
    text-align: center;
}
.com-bar-item .com-writer {
    width: 180px;
    text-align: center;
}
.com-bar-item .com-date {
    width: 150px;
    text-align: center;
}
.none {
    text-decoration: none;
}
</style>
