export default function Reverser(ident, args, onSuccess) {
  let body = {};
  if (ident) {
    body.ident = ident;
    if (args) {
      body.args = args;
    }
  }
  if (body !== {}) {
    body = JSON.stringify(body);
    fetch('/reverse/', {
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
    }).then(
      (response) => response.json()
    ).then(onSuccess)
    .catch(function (err) {
      console.log(err);
    });
  }
}
