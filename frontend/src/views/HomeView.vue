<template>
  <div class="main">

    <div class="leftpane">
      <p class="a">Izaberite žanr</p>

      <GenreButton v-for="g in genres" :genre="g" @genreChanged="changeFilters" />

      <p v-if="moviesFiltered.length == 0">Nema rezultata</p>
      <p v-else-if="moviesFiltered.length == 1">1 rezultat</p>
      <p v-else>{{ moviesFiltered.length }} rezultata</p>
    </div>

    <div class="mainpane">
      <MovieCard v-for="movie in moviesFiltered" :movie="movie" :genres="getGenreNames(movie['genres'])"
        :stars="getStars(movie.id)" />
    </div>

  </div>
</template>

<script>
import axios from 'axios';
import GenreButton from '@/components/GenreButton.vue';
import MovieCard from '@/components/MovieCard.vue';

export default {
  name: 'HomeView',

  components: { GenreButton, MovieCard },

  data() {
    return {
      api_url: '/api/',
      genres: [],
      genresToFilter: [],
      movies: [],
      moviesFiltered: [],
      reviews: [],
    }
  },

  methods: {
    getGenres() {
      axios
        .get(this.api_url + 'genres/')
        .then(response => this.genres = response.data)
        .catch((e) => console.log(e['name'] + ' ' + e['message']))
    },

    getMovies() {
      axios
        .get(this.api_url + 'movies/')
        .then(response => {
          this.movies = response.data
          this.moviesFiltered = response.data
        })
        .catch((e) => console.log(e['name'] + ' ' + e['message']))
    },

    getReviews() {
      axios
        .get(this.api_url + 'reviews/')
        .then(response => this.reviews = response.data)
        .catch((e) => console.log(e['name'] + ' ' + e['message']))
    },

    overlap(arr1, arr2) {
      for (const x of arr1) {
        if (arr2.indexOf(x) > -1) {
          return true
        }
      }
      return false
    },

    refreshMovies() {
      if (this.genresToFilter.length == 0) {
        this.moviesFiltered = this.movies.map(obj => ({ ...obj }))
        return
      }
      this.moviesFiltered = this.movies.filter(
        obj => this.overlap(obj.genres, this.genresToFilter)
      )
    },

    changeFilters(isPressed, id) {
      if (isPressed) {
        this.genresToFilter.push(id)
      } else {
        const index = this.genresToFilter.indexOf(id);
        if (index > -1) {
          this.genresToFilter.splice(index, 1);
        }
      }
      this.refreshMovies()
    },

    getGenreNames(genreIds) {
      const genreNames = []
      for (const id of genreIds) {
        for (const genre of this.genres) {
          if (genre.id == id) {
            genreNames.push(genre.name)
          }
        }
      }
      return genreNames
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
    },
  },

  mounted() {
    this.getGenres()
    this.getMovies()
    this.getReviews()
  },
}
</script>

<style>
p[class="a"] {
  color: #000000;
  font-size: 20px;
  background-color: #FEF047;
  padding: 0;
  text-align: center;
  margin-top: 0px;
}

.main {
  flex: 1;
  display: grid;
  grid-template-columns: 15fr 85fr;
}

.leftpane {
  background-color: #FFFFFF;
  padding-left: 10px;
  padding-right: 10px;
}

.mainpane {
  background-color: #000000;
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
}
</style>
