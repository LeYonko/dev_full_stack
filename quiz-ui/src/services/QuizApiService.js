import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  //première méthode à appeler à l'arrivée sur la Home page
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestion(position) {
    // not implemented
    return this.call("get", "questions?position=" + position);
  },
  postLogin(data){
    return this.call("post", "login", data);
  },
  updateQuestion(data, id, token){
    return this.call("put", "questions/"+id, data, token);
  },
  deleteQuestion(id, token){
    return this.call("delete", "questions/"+id, null, token);
  },
  addQuestion(data, token){
    return this.call("post", "questions", data, token);
  },
  deleteAllQuestions(token){
    return this.call("delete", "questions/all", null, token);
  },
  addParticipation(data){
    return this.call("post", "participations", data);
  },
  deleteAllParticipations(token){
    return this.call("delete", "participations/all", null, token);
  }
};