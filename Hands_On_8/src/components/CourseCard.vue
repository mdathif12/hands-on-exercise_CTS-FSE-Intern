<template>
  <div class="card">
    <h3>{{ name }}</h3>

    <p>
      <strong>Code:</strong> {{ code }}
    </p>

    <p>
      <strong>Credits:</strong> {{ credits }}
    </p>

    <p>
      <strong>Grade:</strong> {{ grade }}
    </p>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  code: String,
  credits: Number,
  grade: String
})
</script>

<style scoped>
.card {
  background: white;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0,0,0,.1);
}
</style>