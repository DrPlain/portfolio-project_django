$(document).ready(function() {

    $('#select-chart-options').change(function () {
        if ($(this).val() === 'Bar chart') {
            $("#nominal-x").show();
            $('#numerical-y').hide();
            $('#color-by').hide();
            $('#numerical-x').hide();
            $('#bin').hide();
            $('#numerical-none').show();

        }
    });
    $('#select-chart-options').change(function () {
        if ($(this).val() === 'Scatter plot') {
            $("#nominal-x").hide();
            $('#color-by').show();
            $('#numerical-x').show();
            $('#numerical-y').show();
            $('#bin').hide();
            $('#numerical-none').hide();
        }
    });
    $('#select-chart-options').change(function () {
        if ($(this).val() === 'Histogram'){
            $("#nominal-x").hide();
            $('#color-by').hide();
            $('#bin').show();
            $('#numerical-y').hide();
            $('#numerical-x').hide();
            $('#numerical-none').show();
        }
    });
    $('#select-chart-options').change(function () {
        if ($(this).val() === 'Line plot') {
            $("#nominal-x").hide();
            $('#color-by').hide();
            $('#bin').hide();
            $('#numerical-y').show();
            $('#numerical-x').show();
            $('#numerical-none').hide();
        }
    });
    $('#select-chart-options').change(function () {
        if ($(this).val() === 'Box plot') {
            $("#nominal-x").hide();
            $('#color-by').hide();
            $('#numerical-x').show();
            $('#numerical-y').hide();
            $('#bin').hide();
            $('#numerical-none').hide();
        }
    });
    $('#select-chart-options').change(function () {
        if ($(this).val() === 'Pie chart') {
            $("#nominal-x").show();
            $('#color-by').hide();
            $('#numerical-x').hide();
            $('#numerical-y').hide();
            $('#bin').hide();
            $('#numerical-none').hide();
        }
    });
    $('#select-chart-options').change(function () {
        if ($(this).val() === 'None') {
            $("#nominal-x").hide();
            $('#color-by').hide();
            $('#numerical-x').hide();
            $('#numerical-y').hide();
            $('#bin').hide();
            $('#numerical-none').hide();
        }
    });
    $("#select-chart-options").trigger("change")


})