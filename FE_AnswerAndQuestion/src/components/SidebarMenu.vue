<template>
  <div class="border rounded-3 me-3 d-flex flex-column" style="height: 100%">
    <h4 class="p-3">Chat A.I +</h4>

    <!-- Nút tạo cuộc hội thoại mới -->
    <Button
      label="New Chat"
      icon="pi pi-plus"
      class="mb-3 ms-3 me-3"
      @click="$emit('clear-chat')"
    />

    <!-- Danh sách cuộc hội thoại -->
    <Menu :model="filteredConversationsMenu" class="mx-3 my-2 overflow-auto flex-grow-1" />
    <!-- Nút cài đặt -->
    <Button label="Settings" icon="pi pi-cog" class="m-3" @click="$emit('open-settings')" />
    <Button label="User" icon="pi pi-user" class="mb-3 ms-3 me-3" @click="$emit('open-profile')" />
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import Button from 'primevue/button'
import { Menu } from 'primevue'

const searchQuery = ref('')
const conversations = ref([
  { id: 1, title: 'Job Suggestions' },
  { id: 2, title: 'CV Feedback' },
  { id: 3, title: 'Interview Tips' },
  { id: 4, title: 'Career Advice' },
  { id: 5, title: 'Skill Development' },
  { id: 6, title: 'Work-Life Balance' },
  { id: 7, title: 'Networking Strategies' },
  { id: 8, title: 'Freelancing Tips' },
  { id: 9, title: 'Remote Work Guide' },
  { id: 10, title: 'Salary Negotiation' },
])

// Lọc cuộc hội thoại theo từ khóa tìm kiếm
const filteredConversations = computed(() =>
  conversations.value.filter((conv) =>
    conv.title.toLowerCase().includes(searchQuery.value.toLowerCase()),
  ),
)
// Map filtered conversations to the format expected by the Menu component
const filteredConversationsMenu = computed(() =>
  filteredConversations.value.map((conv) => ({
    label: conv.title,
    command: () => console.log(`Selected conversation: ${conv.title}`),
  })),
)
</script>
