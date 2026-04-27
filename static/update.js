function addWorkplace() {
    let company = document.getElementById("company").value;
    let term = document.getElementById("term").value;

    if (company === "" || term === "") {
        alert("Заполните все поля");
        return;
    }

    fetch("/add", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            "company": company,
            "term": term
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        location.reload();
    });
}

function deleteWorkplace(id) {
    fetch("/delete/" + id, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        location.reload();
    });
}
