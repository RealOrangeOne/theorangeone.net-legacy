export default function Reverser(ident, args) {
  let body = {};
  if (ident) {
    body.ident = ident;
  }
  if (args) {
    body.args = args;
  }
  body = JSON.stringify(body);
  return fetch('/reverse/', {
    method: 'post',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body
  }).then(function (response) {
    if (response.status === 302) {
      return response;
    } else {
      var error = new Error(response.statusText);
      error.response = response;
      throw error;
    }
  }).then((response) => response.json());
}
