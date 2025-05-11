<!-- ChatInput.vue -->
<template>
  <div class="p-3">
    <div class="d-flex justify-content-center" style="width: 100%">
      <div class="input-group p-2 border" style="max-width: 800px; border-radius: 50px">
        <InputText
          v-model="modelValue"
          placeholder="What's in your mind?"
          class="form-control"
          style="border-radius: 50px; border: none; height: auto; overflow-y: auto"
          :style="{ height: (modelValue?.length ?? 0) > 50 ? 'auto' : '38px' }"
        />
        <Button
          icon="pi pi-send"
          @click="$emit('send-message')"
          class="btn btn-primary"
          style="border-radius: 50px; margin-left: 5px"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'

const props = defineProps<{ modelValue: string }>()
const emit = defineEmits(['update:modelValue', 'send-message'])

const modelValue = defineModel<string>()
</script>
