document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("admissionForm");

    if(form){
        form.addEventListener("submit", async function(e){
            e.preventDefault();

            const formData = new FormData(form);

            try{
                const response = await fetch("/register", {
                    method: "POST",
                    body: formData
                });

                if(response.ok){
                    alert("Admission Submitted Successfully!");
                    form.reset();
                } else {
                    alert("Something went wrong!");
                }

            } catch(error){
                alert("Server Error!");
            }
        });
    }

});