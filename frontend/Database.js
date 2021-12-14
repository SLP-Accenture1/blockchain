let info = '';

let getFunction = () => {
  if (document.getElementById('data') != null) {
    fetch('http://127.0.0.1:3000/database')
    .then(async response => {
        info = await response.json()
        console.log(info)
        str = document.getElementById('data').innerHTML;
        str += '<tr>'
        for (let key in info) {
            str += '<td>' + info[key] + '</td>'
        }
        str += '</tr>'
        console.log(info)
        document.getElementById('data').innerHTML = str
        console.log(str)
    });
  }
}

    /*Make the backend and return some dummy data
    Frontend - change response.text to response.json
    use for loop to iterate over the array and generate child html strings
    set that string into the table's inner html
    add a button (refresh) that will execute getFunction*/
    

// {async () => {
//     const todo = { content };
//     const response = await fetch("/add_todo", {
//     method: "POST",
//     headers: {
//     'Content-Type' : 'application/json'
//     },
//     body: JSON.stringify(todo)
//     }
//   )};
// }

let postFunction = () => async () => {
        const rawResponse = await fetch('http://127.0.0.1:3000', {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(document.getElementById('form_info'))
        });
        const content = await rawResponse.json();
      
        console.log(content);
      };

getFunction();
postFunction();
