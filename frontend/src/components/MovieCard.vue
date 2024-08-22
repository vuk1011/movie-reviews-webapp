<template>
  <div class="card-small">
    <router-link class="card-link" :to="{ name: 'movie', params: { id: movie.id } }">

      <img :src="getImgSrc()" alt="Slika" class="card-small-image">
      <div class="card-small-container">
        <h3 class="card-small-title">{{ movie.title }}</h3>
        <h4>{{ stars }} ⭐</h4>
        <p v-for="genre in genres">{{ genre }}</p>
      </div>

    </router-link>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',

  props: {
    movie: Object,
    genres: Array,
    stars: String,
  },

  methods: {
    getImgSrc() {
      return require(`@/assets/static/${this.$props.movie.id}.jpg`)
    },
  },
}
</script>

<style>
.card-small {
  width: 20vw;
  max-height: 60vw;
  margin: 20px 15px 30px 25px;
  border: 2px solid #89CC04;
  border-radius: 12px;
}

.card-small-image {
  width: 100%;
  height: 28vw;
  border-top-left-radius: 12px;
  border-top-right-radius: 12px;
}

.card-small-container {
  width: 100%;
  min-height: 12vw;
  padding-left: 7px;
  padding-bottom: 7px;
  border-bottom-left-radius: 12px;
  border-bottom-right-radius: 12px;
  font-size: 20px;
  font-style: #FFFFFF;
}

.card-small-title {
  margin: 0px;
}

.card-link {
  color: #FFFFFF;
  text-decoration: none;
}
</style>
