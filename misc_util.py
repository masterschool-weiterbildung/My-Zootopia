import statistics

import constant


def result_message(result: bool, message: str, payload) -> dict:
    return {constant.RESULT: result, constant.MESSAGE: message,
            constant.PAYLOAD: payload}
