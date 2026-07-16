<template>
  <div class="page">

    <h2>{{ course.name }}</h2>

    <p><strong>Code:</strong> {{ course.code }}</p>
    <p><strong>Credits:</strong> {{ course.credits }}</p>
    <p><strong>Grade:</strong> {{ course.grade }}</p>

    <button @click="enrollCourse">
      Enroll Course
    </button>

  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const courses = [
  {
    id: 1,
    name: 'Web Development',
    code: 'IT301',
    credits: 4,
    grade: 'A'
  },
  {
    id: 2,
    name: 'Database Systems',
    code: 'IT302',
    credits: 3,
    grade: 'A+'
  },
  {
    id: 3,
    name: 'Cloud Computing',
    code: 'IT303',
    credits: 4,
    grade: 'A'
  },
  {
    id: 4,
    name: 'Cyber Security',
    code: 'IT304',
    credits: 3,
    grade: 'B+'
  },
  {
    id: 5,
    name: 'Machine Learning',
    code: 'IT305',
    credits: 4,
    grade: 'A'
  }
]

const course =
  courses.find(
    c => c.id === Number(route.params.id)
  ) || {}

function enrollCourse() {
  router.push('/profile')
}
</script>

<style scoped>
button {
  background: green;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}
</style>