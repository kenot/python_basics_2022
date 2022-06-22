volume_v_of_the_pool = int(input())
debit_of_first_pipe = int(input())
debit_of_second_pipe = int(input())
hours_h_of_missing = float(input())

first_pipe_volume_filled = hours_h_of_missing * debit_of_first_pipe # 300

second_pipe_volume_filled = hours_h_of_missing * debit_of_second_pipe # 360

total_volume_filled_while_worker_missing = first_pipe_volume_filled + second_pipe_volume_filled # 660
total_volume_filled_while_worker_missing_in_percent = (total_volume_filled_while_worker_missing * 100) / volume_v_of_the_pool # 66

first_pipe_volume_filled_in_percent = (first_pipe_volume_filled * 100) / total_volume_filled_while_worker_missing
second_pipe_volume_filled_in_percent = (second_pipe_volume_filled * 100) / total_volume_filled_while_worker_missing

liters_surplus = 0

if total_volume_filled_while_worker_missing <= volume_v_of_the_pool:
    print(f"The pool is {total_volume_filled_while_worker_missing_in_percent:.2f}% full. Pipe 1: {first_pipe_volume_filled_in_percent:.2f}%. Pipe 2: {second_pipe_volume_filled_in_percent:.2f}%.")
else:
    liters_surplus = abs(total_volume_filled_while_worker_missing - volume_v_of_the_pool)
    print(f"For {hours_h_of_missing:.2f} hours the pool overflows with {liters_surplus:.2f} liters.")


