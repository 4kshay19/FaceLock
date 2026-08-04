<script src="{{ url_for('static', filename='js/register.js') }}"></script>
startCamera()

captureFace()

registerFace()
let progress = 0;

function updateProgress(value){
    progress = value;

    const bar = document.getElementById("progressBar");

    bar.style.width = value + "%";

    bar.innerHTML = value + "%";
}
function simulateRegistration(){

    updateProgress(25);

    document.getElementById("cameraStatus").innerHTML =
    "📷 Camera Ready";

    setTimeout(function(){

        updateProgress(50);

        document.getElementById("faceStatus").innerHTML =
        "😀 Face Detected";

    },1000);

    setTimeout(function(){

        updateProgress(75);

        document.getElementById("captureStatus").innerHTML =
        "📸 Image Captured";

    },2000);

    setTimeout(function(){

        updateProgress(100);

        document.getElementById("saveStatus").innerHTML =
        "💾 Face Saved Successfully";

        document.getElementById("messageBox").innerHTML =
        "✅ Registration Completed";

    },3000);

}
console.log("register.js loaded successfully!");