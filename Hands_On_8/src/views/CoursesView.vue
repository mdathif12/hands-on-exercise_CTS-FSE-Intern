<template>
  <div class="page">

    <h2>Available Courses</h2>

    <input
      v-model="searchTerm"
      placeholder="Search course..."
      class="search"
    />

    <div class="grid">

      <div
        v-for="course in filteredCourses"
        :key="course.id"
      >
        <CourseCard
          :name="course.name"
          :code="course.code"
          :credits="course.credits"
          :grade="course.grade"
        />

        <div class="actions">
          <RouterLink :to="`/courses/${course.id}`">
            View Details
          </RouterLink>

          <button @click="store.enroll(course)">
            Enroll
          </button>
        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import CourseCard from '../components/CourseCard.vue'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

const courses = ref([])
const searchTerm = ref('')

onMounted(() => {
  courses.value = [
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
})

const filteredCourses = computed(() =>
  courses.value.filter(course =>
    course.name
      .toLowerCase()
      .includes(searchTerm.value.toLowerCase())
  )
)
</script>

<style scoped>
.search {
  width: 100%;
  padding: 12px;
  margin: 20px 0;
}

.grid {
  display: grid;
  grid-template-columns:
    repeat(auto-fit,minmax(250px,1fr));
  gap: 20px;
}

.actions {
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
}

button {
  background: #2563eb;
  color: white;
  border: none;
  padding: 8px 15px;
  cursor: pointer;
}
</style>