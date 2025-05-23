// static/js/main.js
async function askQuestion() {
    const question = document.getElementById("question").value;
    const imagePath = document.querySelector("img").getAttribute("src");

    const response = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ question, image_path: imagePath }),
    });

    const data = await response.json();
    document.getElementById("answer").innerText = data.answer;
}

async function useVoice() {
    const response = await fetch("/voice");
    const data = await response.json();
    document.getElementById("question").value = data.question;
    askQuestion();
}
