export default function Reverser(ident) {
  return fetch('/reverse/', {
    method: 'post',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ident})
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
