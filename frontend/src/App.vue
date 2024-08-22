<template>
  <div class="wrapper">

    <div class="header">
      <h1 class="header-text">Domaći Filmovi</h1>
      <p class="header-text">pretražite i ocenite domaće filmove</p>
    </div>

    <RouterView></RouterView>

    <div class="footer">
      <p>Copyright (c) 2024</p>
    </div>

  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
.header {
  padding: 40px;
  text-align: left;
  background: #FFFFFF;
  padding-left: 25%;
  margin: 0px;
}

.header-text {
  color: black;
}

h1[class="header-text"] {
  font-size: 40px;
}

p[class="header-text"] {
  font-size: 25px;
  color: #6B717E;
}

.footer {
  padding: 20px;
  text-align: center;
  background: #FFFFFF;
  margin: 0px;
}
</style>
