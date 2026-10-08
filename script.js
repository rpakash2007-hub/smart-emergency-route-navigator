function scrollToRoute() {

    document.getElementById("route").scrollIntoView({
        behavior: "smooth"
    });

}


function findRoute() {

    const start = document.getElementById("startLocation").value;
    const destination = document.getElementById("destination").value;
    const emergency = document.getElementById("emergencyLevel").value;

    if (start === "" || destination === "") {

        alert("Please enter ambulance location and destination.");

        return;
    }


    // Demo route calculation
    let distance = "8.5 km";
    let time = "12 minutes";
    let traffic = "Medium";

    if (emergency === "high") {

        time = "9 minutes";
        traffic = "Priority Route";

    } 
    else if (emergency === "medium") {

        time = "11 minutes";
        traffic = "Medium";

    } 
    else {

        time = "14 minutes";
        traffic = "Normal";

    }


    document.getElementById("distance").innerText = distance;

    document.getElementById("time").innerText = time;

    document.getElementById("trafficStatus").innerText = traffic;

    document.getElementById("routeStatus").innerText =
        "Fastest Route Found ✓";

}