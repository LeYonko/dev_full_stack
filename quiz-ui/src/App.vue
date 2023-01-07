<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    
    <div class="wrapper">
      
        <div class="font-sans antialiased" id="app">
            <nav class="flex items-center flex-wrap bg-gradient-to-r from-indigo-400 via-purple-500 to-pink-500 p-6">
                <div class="flex items-center flex-no-shrink text-white mr-6">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-8 h-8 mr-3" >
                        <path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5" />
                    </svg>
                    <span class="font-semibold text-xl">Quiz App</span>
                </div>
                <div class="absolute right-10 text-sm items-end justify-end">
                    <RouterLink to="/" class="mt-4 text-white hover:text-amber-200 mr-4">
                    Page d'accueil
                    </RouterLink>
                    <RouterLink to="/aboutUs" class="mt-4 text-white hover:text-amber-200 mr-4">
                    Qui sommes-nous ?
                    </RouterLink>
                    <RouterLink to="/admin" class="text-sm px-4 py-2 border-2 rounded-lg text-white border-white hover:bg-opacity-40 hover:bg-white">Connexion</RouterLink>
                </div>
            </nav>
        </div>

    </div>
  </header>

  <RouterView />
</template>