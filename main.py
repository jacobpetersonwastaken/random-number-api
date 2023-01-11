from random import uniform

def lambda_handler(event, context):
    # TODO implement
    text = event["queryStringParameters"]["rand_num"]
    min, max, count = 0, 100, 1
    values = {"min": min, "max": max, "count": count}
    text_formatted = text.split(" ")

    def success(r):
        return {
            "statusCode": 200,
            "body": str(r)
        }

    if len(text_formatted) > 1:
        for i, x in enumerate(text_formatted):
            try:
                if float(x):
                    values[list(values.keys())[i]] = float(x)
            except ValueError:
                return success(f"Correct format is 0 50 0 | min max count {round(uniform(min, max), 4)}")
        if values["count"] > 10:
            values["count"] = 10
        return success([round(uniform(values["min"], values["max"]), 4) for _ in range(int(values["count"]))])

    if len(text_formatted) == 1 and text_formatted[0].isnumeric():
        values["max"] = float(text_formatted[0])
        return success(round(uniform(values["min"], values["max"]), 4))

    if text_formatted:
        return success(round(uniform(values["min"], values["max"]), 4))