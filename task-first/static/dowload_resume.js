    // getCookie Provided by Django in the Official Docs
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');


    // Setting the Click Event Listener on the Submit Button
    $('[type="submit"]').on('click', function (e) {
        e.preventDefault()
        // Making the AJAX Request
        $.ajax({
            url: $("form")[0].action,
            type: "POST",
            data: {
                name: $("#id_name")[0].value,
            },
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function (data) {
                console.log(data);
            },
            error: function (error) {
                console.log(error);
            }
        });
    })
