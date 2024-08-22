<template>
  <div class="top-bar">
    <router-link class="link-back" :to="{ name: 'home' }">
      < Nazad
    </router-link>
  </div>

  <div class="card-big">
    <img class="card-big-image" :src="getImgSrc()" alt="Slika">
    <div class="card-big-container">
      <h2>{{ movie.title }} ({{ movie.year }})</h2>
      <h3>{{ getStars($route.params.id) }} ⭐</h3>
      <hr>
      <h3>Opis</h3>
      <p>{{ movie.description }}</p>
      <hr>
      <h3>Glumci</h3>
      <p>{{ movie.actors }}</p>
      <hr>
      <h4>Žanrovi</h4>
      <i>{{ genres.join(', ') }}</i>
    </div>
  </div>

  <ReviewForm :reviews="reviews" :movie="movie.id"/>
</template>

<script>
import axios from 'axios';
import ReviewForm from '@/components/ReviewForm.vue'

export default {
  name: 'MovieView',

  components: { ReviewForm },
  
  data() {
    return {
      movie: {},
      api_url: '/api/',
      genres: [],
      reviews: [],
    }
  },

  methods: {
    getMovie() {
      axios
        .get(`${this.api_url}movies/${this.$route.params.id}/`)
        .then(response => {
          this.movie = response.data
          this.getGenres()
        })
        .catch((e) => console.log(e['name'] + ' ' + e['message']))
    },
    getImgSrc() {
      return require(`@/assets/static/${this.$route.params.id}.jpg`)
    },
    movieHasGenre(genreId) {
      return this.movie.genres.indexOf(genreId) > -1
    },
    getGenres() {
      axios
        .get(`${this.api_url}genres/`)
        .then(response => {
          for (const g of response.data) {
            if (this.movieHasGenre(g.id)) {
              this.genres.push(g.name)
            }
          }
        })
    },
    getReviews() {
      axios
        .get(`${this.api_url}reviews/`)
        .then(response => {
          this.reviews = response.data.filter(
            rev => rev.movie == this.$route.params.id
          )          
        })
        .catch((e) => console.log(e['name'] + ' ' + e['message']))
    },
    getStars(movieId) {
      let reviewsFiltered = this.reviews.filter(r => r.movie == movieId)
      if (reviewsFiltered.length == 0) {
        return '-'
      }
      let sum = 0
      for (const r of reviewsFiltered) {
        sum += r.stars
      }
      return (sum / reviewsFiltered.length).toFixed(1)
    }
  },

  mounted() {
    this.getMovie()
    this.getReviews()
  },
}
</script>

<style>
.link-back {
  text-decoration: none;
  font-size: 25px;
  color: #FEF047;
}

.top-bar {
  align-self: center;
  padding: 20px;
}

.card-big {
  margin: 15px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  padding: 15px;
  border: 2px solid #FEF047;
  border-radius: 10px;
  align-items: center;
  justify-items: center;
}

.card-big-image {
  max-width: 85%;
  max-height: 80vh;
}

.card-big-container {
  color: #FFFFFF;
}

.card-big-container > h2 {
  font-size: 30px;
}

.card-big-container > h3 {
  font-size: 25px;
}

.card-big-container > h4 {
  font-size: 20px;
}

.card-big-container > i {
  font-size: 18px;
}

.card-big-container > p {
  font-family: Arial, Helvetica, sans-serif;
}

hr {
  color: #FEF047;
}
</style>