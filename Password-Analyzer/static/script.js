const passwordInput = document.getElementById("password");
const toggleButton = document.getElementById("toggle-password");
const bar = document.getElementById("progress-bar");
const strength = document.getElementById("strength");
const scoreText = document.getElementById("score-text");
const entropy = document.getElementById("entropy");
const breachStatus = document.getElementById("breach-status");
const dictionaryStatus = document.getElementById("dictionary-status");
const feedback = document.getElementById("feedback");

toggleButton.addEventListener("click", () => {
    if(passwordInput.type === "password"){
        passwordInput.type = "text";
        toggleButton.textContent = "Hide";
    }else{
        passwordInput.type = "password";
        toggleButton.textContent = "View";
    }
});

passwordInput.addEventListener("input", async () => {
    const password = passwordInput.value;
    if (password.length === 0) {
        bar.style.width = "0%";
        strength.textContent = "Waiting for input...";
        scoreText.textContent = "0 / 20";
        entropy.textContent = "-- bits";
        breachStatus.textContent = "Waiting...";
        dictionaryStatus.textContent = "Waiting...";
        feedback.innerHTML = "";
        return;
    }

    try {
        const response = await fetch("/check", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
			
            body: JSON.stringify({
                password: password
            })

        });
		

        const data = await response.json();
        const percentage = (data.score / data.max_score) * 100;
        
		bar.style.width = percentage + "%";
        bar.style.background = data.color;

        strength.textContent = data.strength;

        scoreText.textContent =
            `${data.score} / ${data.max_score}`;

        entropy.textContent =
            `${data.entropy.toFixed(2)} bits`;

        if (data.breach_count === null) {
            breachStatus.textContent =
                "Unable to check";
        } else if (data.breached) {
            breachStatus.textContent =
                `Found ${data.breach_count.toLocaleString()} times`;
        } else {
            breachStatus.textContent =
                "Not Found";
        }

        if (data.feedback.some(f => f.toLowerCase().includes("dictionary"))) {
            dictionaryStatus.textContent =
                "Dictionary word detected";
        } else {
            dictionaryStatus.textContent =
                "None";
        }

        feedback.innerHTML = "";

        data.feedback.forEach(item => {
            const li = document.createElement("li");
            li.textContent = item;
            feedback.appendChild(li);
        });

    } catch (error) {
        console.error(error);
    }

});