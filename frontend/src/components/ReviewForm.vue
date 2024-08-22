<template>
  <div class="form-wrapper">
    <form @submit.prevent="handleSubmit">

      <h2>Ocenite ovaj film</h2>
      <label>Email:</label>
      <br>
      <input type="email" required v-model="email">
      <br>

      <label>Ocena:</label>
      <br>
      <input type="number" min="0" max="10" required v-model="stars">
      <br>

      <button class="btn-submit">Pošalji ocenu</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
 
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

export default {
  name: 'ReviewForm',

  data() {
    return {
      email: '',
      stars: 10,
      api_url: '/api/',
    }
  },

  props: {
    reviews: {
      type: Array,
      required: true,
    },
    movie: {
      type: Number,
      required: true,
    },
  },

  methods: {
    handleSubmit() {
      // check if the user already posted
      const emails = this.reviews.map(rev => rev.email)
      if (emails.indexOf(this.email) > -1) {
        alert('Već ste uneli Vašu ocenu!')
      } else {
        const csrfToken = getCookie('csrftoken');

        axios
          .post(this.api_url + 'reviews/', {
            email: this.email,
            stars: this.stars,
            movie: this.movie
          }, {
            headers: {
              'X-CSRFToken': csrfToken
            }
          })
          .then(response => {})
          .catch((e) => console.log(e['name'] + ' ' + e['message']))
      }
      location.reload()
    }
  },
}
</script>

<style>
.form-wrapper {
  width: 100vw;
  background-color: #FEF047;
  align-self: center;
}

form {
  margin: 30px;
}

form > h2 {
  font-size: 30px;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: 400;
  margin-bottom: 20px;
}

label {
  font-size: 22px;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: 100;
}

form > h2 label {
  color: #000000;
}

form > * {
  margin: 5px;
}

input {
  background-color: transparent;
  color: #000000;
  border: 2px dashed #000000;
  width: 150px;
  height: 17px;
}

button.btn-submit {
  background-color: #000000;
  color: #FEF047;
  width: 150px;
  height: 20px;
  border: none;
}

button.btn-submit:hover {
  background-color: #FFFFFF;
  color: #000000;
}
</style>