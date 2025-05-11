<template>
  <div class="p-4">
    <div class="mb-4 d-flex align-items-start" v-for="(msg, index) in messages" :key="index">
      <img
        :src="
          msg.sender === 'User'
            ? 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/User-avatar.svg/2048px-User-avatar.svg.png'
            : 'https://cdn.oaistatic.com/assets/sora-mutf8tav.webp'
        "
        alt="avatar"
        class="me-3 rounded-circle"
        style="width: 40px; height: 40px"
      />
      <div style="width: 100%">
        <div class="fw-bold mb-1">{{ msg.sender }}</div>
        <div v-if="msg.sender === 'Chat A.I+'">
          <div class="context-text">
            {{ msg.text }}
          </div>
          <Button
            v-if="msg.text"
            @click="findQuestion(index)"
            style="font-size: 14px; float: right"
          >
            Find
          </Button>
        </div>
        <div class="context-text" v-else>
          {{ msg.text }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue'
import { Button } from 'primevue'

defineProps<{ messages: { sender: string; text: string }[] }>()

const findQuestion = (index: number) => {
  const previousMessage = document.querySelectorAll('.context-text')[index - 1]
  const currentMessage = document.querySelectorAll('.context-text')[index]
  if (currentMessage && previousMessage) {
    const currentText = currentMessage.textContent || ''
    const previousText = previousMessage.textContent || ''

    if (previousMessage.innerHTML.includes(`<strong>${currentText}</strong>`)) {
      previousMessage.innerHTML = previousText
    } else if (previousText.includes(currentText)) {
      const highlightedText = previousText.replace(currentText, `<strong>${currentText}</strong>`)
      previousMessage.innerHTML = highlightedText
    }
  }
}
</script>
