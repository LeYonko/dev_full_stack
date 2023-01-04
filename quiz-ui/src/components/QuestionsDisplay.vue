<template>
    <img v-if="question.image" :src="question.image" />
    <br />
    <br />
    <div v-for="answer, idx in this.question.possibleAnswers" v-bind:key="answer.id">
        <ul>
            <li @click="chosenAnswer(idx+1)">{{ answer.text }}</li>
        </ul>
    </div>
    
</template>

<script>

export default {

    props: {
        question: {
            type: Object
    },
    total: {
        type: String
    }
},
name: "AnswerEmit",
emits: ["answer-selected"],
data(){
    return{

    }
},
methods:{
    chosenAnswer(answerNum){
        this.$emit('answer-selected', answerNum);
    }
}
};
</script>