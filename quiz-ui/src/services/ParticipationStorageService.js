export default {
    clear() {
        //window.localStorage.clear();
        window.localStorage.removeItem("playerName");
        window.localStorage.removeItem("participationScore");
        window.localStorage.removeItem("participationAnswers");
        window.localStorage.removeItem("goodAnswers");
    },
    savePlayerName(playerName) {
          window.localStorage.setItem("playerName", playerName);
    },
    getPlayerName() {
          return window.localStorage.getItem("playerName");
    },
    saveParticipationScore(participationScore) {
          window.localStorage.setItem("participationScore", participationScore);
    },
    getParticipationScore() {
          return window.localStorage.getItem("participationScore");
    },
    saveParticipationAnswers(participationAnswers) {
        window.localStorage.setItem("participationAnswers", participationAnswers);
    },
    getParticipationAnswers() {
            return window.localStorage.getItem("participationAnswers");
    },
    saveGoodAnswers(goodAnswers) {
        window.localStorage.setItem("goodAnswers", goodAnswers);
    },
    getGoodAnswers() {
            return window.localStorage.getItem("goodAnswers");
    },
    saveToken(token){
        window.localStorage.setItem("token", token);
    },
    getToken(){
        return window.localStorage.getItem("token");
    },
  };