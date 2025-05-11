<template>
  <div class="d-flex vh-90 border rounded-3 p-3" style="margin: 45px 250px; border-radius: 20px">
    <SidebarMenu @clear-chat="handleClearChat" />
    <div class="flex-grow-1 d-flex flex-column border rounded-3">
      <ChatHeader />
      <ChatMessages :messages="messages" class="flex-grow-1 overflow-auto" />
      <ChatInput v-model="message" @send-message="handleSendMessage" />
    </div>
  </div>
</template>

<script setup lang="ts">
import ChatHeader from '../components/ChatHeader.vue'
import SidebarMenu from '@/components/SidebarMenu.vue'
import ChatMessages from '../components/ChatMessages.vue'
import ChatInput from '../components/ChatInput.vue'
import { ref } from 'vue'

const message = ref('')
const messages = ref<{ sender: string; text: string }[]>([])

const handleClearChat = () => {
  messages.value = []
}

const handleSendMessage = async () => {
  if (!message.value.trim()) return

  messages.value.push({ sender: 'User', text: message.value })

  const questionIndex = message.value.indexOf('?')
  const context =
    questionIndex !== -1
      ? message.value.substring(0, message.value.lastIndexOf('.', questionIndex) + 1).trim()
      : ''
  const question =
    questionIndex !== -1
      ? message.value
          .substring(message.value.lastIndexOf('.', questionIndex) + 1, questionIndex + 1)
          .trim()
      : ''

  const payload = { context: context || '', question: question || '' }

  try {
    const response = await fetch('http://localhost:8000/qa', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    })

    if (response.ok) {
      const data = await response.json()
      messages.value.push({
        sender: 'Chat A.I+',
        text: data.answer || 'No response',
      })
    } else {
      messages.value.push({ sender: 'Chat A.I+', text: 'Error: ' + response.statusText })
    }
  } catch (error) {
    messages.value.push({ sender: 'Chat A.I+', text: 'Fetch error: ' + String(error) })
  }

  message.value = ''
}
</script>

<style scoped>
.vh-90 {
  height: 90vh;
}
</style>
