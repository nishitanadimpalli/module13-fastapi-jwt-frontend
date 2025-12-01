document.getElementById("loginForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const msg = document.getElementById("message");
    msg.innerText = "";

    const response = await fetch("/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            email: email,
            password: password
        })
    });

    const data = await response.json();

    if (response.ok) {
        msg.innerText = "Login successful!";
        msg.style.color = "green";
        console.log("JWT TOKEN:", data.access_token);
        localStorage.setItem("token", data.access_token);
    } else {
        msg.innerText = data.detail;
        msg.style.color = "red";
    }
});
