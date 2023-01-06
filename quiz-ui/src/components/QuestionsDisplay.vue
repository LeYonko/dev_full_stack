<template>
    <div class="ml-6 mt-2">
      <h1>
        <div class="font-semibold text-xl">Question {{question.position}} : {{question.title}}</div>
      </h1> 
      <br>
    </div>
    <div class="ml-6">
        <img style="width:500px; height:300px" v-if="question.image" :src="question.image" />
    </div>
    <br>
    <div class="font-semibold text-xl ml-6 mr-6 px-4 py-2 border-2 rounded-lg text-black border-blue-500 bg-gray-50/75">{{question.text}}</div>
    <br />
    <div class="grid grid-cols-2 gap-12">
        <div v-for="answer, idx in this.question.possibleAnswers" v-bind:key="answer.id">
            <button type="button" @click="chosenAnswer(idx+1)" :class="[this.selectedAnswer === idx+1 ? 'border-green-600 hover:bg-green-400 bg-green-400/50' : 'border-blue-600 hover:bg-blue-400 bg-sky-400/50']" class="w-1/2 px-5 py-5 font-bold col-span-1 ml-6 mr-6 border-2 rounded-lg text-black hover:bg-opacity-40">
                {{ answer.text }}
            </button>
        </div>
    </div>
    <br>
    <div v-if="question.position == numberOfQuestion">
        <div class="flex">
            <button type="button" @click="validationAnswer" class="w-30
                px-6
                py-3
                bg-blue-600
                text-white
                font-medium
                text-xs
                uppercase
                rounded
                hover:bg-blue-700
                ml-6
                mb-6">Fin du quiz
            </button>
        </div>
    </div>
    <div v-else>
        <div class="flex">
            <button type="button" @click="validationAnswer" class="w-30
                px-6
                py-3
                bg-blue-600
                text-white
                font-medium
                text-xs
                uppercase
                rounded
                hover:bg-blue-700
                ml-6
                mb-6">Question suivante
            </button>
        </div>
    </div>
    <br>
</template>

<script>

export default {

    props: {
        question: {
            type: Object
        },
        numberOfQuestion: {
            type: String
        }
    },
    name: "AnswerEmit", //optionel
    emits: ["answer-selected"],
    data(){
        return{
            selectedAnswer: 0,
        }
    },
    methods:{
        chosenAnswer(position){
            console.log(position);
            this.selectedAnswer = position;
        },
        validationAnswer(){
            this.$emit('answer-selected', this.selectedAnswer);
            this.selectedAnswer = 0;
        }
    }
};

</script>