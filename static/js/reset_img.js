$(function () {
    $('img').each(function () {
        var imagepath = $(this).attr('src')
        imagepath = "{% static '" + imagepath + "' %}"
        $(this).attr('src',imagepath)

    })
    console.log($('body').html())
})