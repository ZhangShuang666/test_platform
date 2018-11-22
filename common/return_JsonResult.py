from django.http import JsonResponse


def response_success(message="请求成功", data={}):
    """
    返回成功结果
    :param message:
    :param data:
    :return: json结果
    """
    content = {
        "success": "true",
        "message": message,
        "data": data
    }
    return JsonResponse(content)


def response_false(message="请求失败"):
    """
    返回失败的结果
    :param message:
    :return: json结果
    """
    content = {
        "success": "false",
        "message": message
    }
    return JsonResponse(content)