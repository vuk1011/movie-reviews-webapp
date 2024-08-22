<template>
  <div class="genre-button-wrapper">
	<button
		class="genre-btn"
		@click="changeStatus()"
			:class="{pressed: isPressed}"
		>
			{{ genre.name }}
		</button>
  </div>
</template>

<script>
export default {
  name: 'GenreButton',

  props: {
    genre: Object
  },

  data() {
    return {
			isPressed: false,
    }
  },

	methods: {
		changeStatus() {
			this.isPressed = !this.isPressed
			this.$emit('genreChanged', this.isPressed, this.$props.genre.id)
		}
	},
}
</script>

<style>
.genre-btn {
	font-size: 18px;
	background-color: #FFFFFF;
	padding: 3px 7px 3px 7px;
	border-radius: 11px;
	border: 1px solid #6B717E;
}

.genre-btn.pressed {
	background-color: #89CC04;
	border: 2px solid #000000;
}

.genre-button-wrapper {
	padding: 0;
	margin-top: 5px;
}
</style>