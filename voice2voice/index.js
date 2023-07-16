// solve: Uncaught ReferenceError: apigClientFactory is not defined at index.js:5:20
// const apigClientFactory = require("./apiGateway-js-sdk/apigClient").default;
// const apigClient = apigClientFactory.newClient();

// const API_URL = "https://1rup48u854.execute-api.us-east-1.amazonaws.com/v1";
const API_URL = "https://7a32l4znb7.execute-api.us-east-1.amazonaws.com/v1";

const recordButton = document.querySelector("#record");
const transcriptInput = document.querySelector("#transcript");

window.SpeechRecognition =
	window.webkitSpeechRecognition || window.SpeechRecognition;
const recognition = new window.SpeechRecognition();
recognition.interimResults = true;

let finalTranscript = "";
let isRecording = false;

recognition.addEventListener("result", (e) => {
	const transcript = Array.from(e.results)
		.map((result) => result[0])
		.map((result) => result.transcript)
		.join("");

	if (e.results[0].isFinal) {
		finalTranscript += transcript;
	}
});

recognition.addEventListener("end", () => {
	transcriptInput.value = finalTranscript;
});

recordButton.addEventListener("click", () => {
	if (isRecording) {
		recognition.stop();
		recordButton.textContent = "Start Recording";
	} else {
		finalTranscript = "";
		recognition.start();
		recordButton.textContent = "Stop Recording";
	}
	isRecording = !isRecording;
});

const searchButton = document.querySelector("#search");
searchButton.addEventListener("click", () => {
	const transcript = transcriptInput.value;
	console.log(transcript);
	// make a get call to this url ${API_URL}/search?q=${transcript} and print the response body
	fetch(`${API_URL}/search?q=${transcript}`, {
		method: "GET",
		headers: {
			"x-api-key": "bojackhorsemanpeanutbutter",
		},
	})
		.then((response) => response.json())
		.then((data) => {
			console.log(data);
			const results = document.querySelector("#results");
			results.innerHTML = "";
			data.results.forEach((item) => {
				const div = document.createElement("div");
				const img = document.createElement("img");
				img.style.height = "200px";
				img.style.float = "left";
				img.style.margin = "5px";
				img.src = item;
				div.appendChild(img);
				results.appendChild(div);
			});
		});
});

const text2speechButton = document.querySelector("#text2speechbutton");
text2speechButton.addEventListener("click", () => {
    // get the text2speech_text value
    const text2speech_text = document.querySelector("#text2speech_text").value;
    console.log(text2speech_text);
    var msg = new SpeechSynthesisUtterance();
    msg.text = text2speech_text;
    window.speechSynthesis.speak(msg);
});

const translationButton = document.querySelector("#translationbutton");
translationButton.addEventListener("click", () => {
    // get the translation_text value
    const translation_text = document.querySelector("#translation_text").value;
    console.log(translation_text);
    // get the input language and output language
    const input_language = document.querySelector("#input_language").value;
    const output_language = document.querySelector("#output_language").value;
    console.log(input_language);
    console.log(output_language);
});

const uploadButton = document.querySelector("#upload");
uploadButton.addEventListener("click", () => {
	const file = document.querySelector("#file").files[0];
	const customLabels = document.querySelector("#custom_labels");
	console.log(file);
	const fileName = file.name;
	const customLabelsValue = customLabels.value;
	console.log(fileName);
	console.log(file);
	console.log(customLabelsValue);
	customLabels.value = "";

	if (
		file.type !== "image/jpeg" &&
		file.type !== "image/png" &&
		file.type !== "image/jpg"
	) {
		alert("Please upload a valid file type (jpg, png, or jpeg)");
	} else {
		const reader = new FileReader();
		reader.onload = () => {
			// const base64Img = btoa(event.target.result);
			// console.log(base64Img);
			console.log(reader.result);
			fetch(
				`${API_URL}/upload`,
				// "https://we08oh48pc.execute-api.us-east-1.amazonaws.com/v1/upload",
				{
					method: "PUT",
					headers: {
						"Content-Type": file.type,
						bucket: "cs6998-hw2-stack-imagess3bucket-74agfgc7zwro",
						key: fileName,
						"x-amz-meta-customLabels": customLabelsValue,
					},
					body: reader.result,
				}
			)
				.then((response) => {
					console.log(response);
				})
				.catch((err) => {
					console.log(err);
				});
		};
		reader.readAsArrayBuffer(file);
	}

});