import pendulum as pdl


def format_to_2_decimal(value: float) -> str:
    # NOTE: disregarding exact precision
    return "{:.2f}".format(value)


def should_prev_wed_shift_backwards(now: pdl.DateTime):
    prev_wed = now.previous(pdl.WEDNESDAY).end_of('day')
    prev_tues = now.previous(pdl.TUESDAY).end_of('day')
    return prev_wed > prev_tues
