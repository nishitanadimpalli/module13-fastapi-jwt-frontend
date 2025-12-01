document.getElementById("registerForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const confirm = document.getElementById("confirm").value;

    const msg = document.getElementById("message");
    msg.innerText = "";

    if (password !== confirm) {
        msg.innerText = "Passwords do not match";
        msg.style.color = "red";
        return;
    }

    const response = await fetch("/users/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            email: email,
            username: username,
            password: password
        })
    });

    const data = await response.json();

    if (response.ok) {
        msg.innerText = "Registration successful!";
        msg.style.color = "green";
    } else {
        msg.innerText = data.detail;
        msg.style.color = "red";
    }
});
