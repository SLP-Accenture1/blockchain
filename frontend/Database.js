let data = '';

let getFunction = () => {
    fetch('http://192.168.0.187:3000/database')
    //.then(response => response.json())
    .then(async response => {
        data = await response.text()
        console.log(data)

    });
}

getFunction()
