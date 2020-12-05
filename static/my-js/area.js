//初始化方法

var address = ''

$(function () {
    //查询所有的省份信息
    $.ajax({
        url: "/sm/selProvince",
        type: "GET",
        data: {},
        success: function (data) {
            dataNow = JSON.parse(data)
            var result = "<option value=''>选择省份</option>";
            $.each(dataNow, function (n, value) {
              /*  if(value.code=='130000')
                    result += "<option selected value=" + value.code + ">" + value.name + "</option>";
                else */
                 result += "<option value=" + value.code + ">" + value.name + "</option>";
            });
            $("#province").html('');       //清空操作，可以使用下边的.empty()方法
            $("#province").append(result);
        }
    });
});
//根据所选择的省份信息选择市信息
$("#province").change(function () {
    var post_data = {
        provinceCode: $("#province").val(),
    };
    if (post_data.provinceCode == null) {
        alert('请选择对应的省')
    }
    $.ajax({
        url: "/sm/selCity",
        type: "GET",
        data: post_data,
        success: function (data) {
            dataNow = JSON.parse(data)
            var result = "<option value=''>选择城市</option>";
            $.each(dataNow, function (n, value) {
                result += "<option value=" + value.code + ">" + value.name + "</option>";
            });
            $("#city").html('');       //清空操作，可以使用下边的.empty()方法
            $("#county").html('');       //清空操作
            $("#city").append(result);

            address = $("#province").find("option:selected").text()
            $("#address").val(address)

        }
    })
})
//根据所选择的市信息选择区信息
$("#city").change(function () {

    var post_data = {
        cityCode: $("#city").val(),
    };
    if (post_data.cityCode == null) {
        alert('请选择对应的城市')
    }
    $.ajax({
        url: "/sm/selCounty",
        type: "GET",
        data: post_data,
        success: function (data) {
            dataNow = JSON.parse(data)
            var result = "<option value=''>选择区县</option>";
            $.each(dataNow, function (n, value) {
                result += "<option value=" + value.code + ">" + value.name + "</option>";
            });
            $("#county").html('');       //清空操作，可以使用下边的.empty()方法
            $("#county").append(result);

            address = $("#province").find("option:selected").text() + $("#city").find("option:selected").text()
            $("#address").val(address)
        },
        error: function () {
            alert("ddddd")
        }
    })
})

//区县信息下拉框改变，触发的函数
$("#county").change(function () {
    address = $("#province").find("option:selected").text() + $("#city").find("option:selected").text() + $("#county").find("option:selected").text()
    $("#address").val(address)
})


$("#address_detail").on('blur', function () {
    address_detail_convert($("#address_detail").val())
})


function address_detail_convert(address_detail) {
    $.ajax({
        url: "https://restapi.amap.com/v3/geocode/geo?key=90399ab66739c726178be0a303717e48&s=rsv3&city=35&address=" + address_detail,
        type: "GET",
        data: {},
        success: function (result) {
            var geocodes = result['geocodes']
            if (geocodes != null && geocodes != '') {
                var local = geocodes[0]['location']  //获取地址的经纬度(例如78.262,95.222)
                var points = local.split(',')
                $("#lon").empty()
                $("#lat").empty()
                $("#lon").val(points[0])  // 经度
                $("#lat").val(points[1])  // 纬度
            }else{
                alert("定位失败！请输入有效的详细地址")
            }
        }
    })

}
