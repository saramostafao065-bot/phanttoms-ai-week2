def process_team_scores(scores_list):
  try:
    if not scores_list:
      return 0, []

    total = 0
    passed = []

    for score in scores_list:
      total += score
      if score >= 50:
        passed.append(score)

    avg = total / len(scores_list)
    return avg, passed

  except Exception:
    return 0, []


test_data = [45, 50, 75, 90, 60]
print(process_team_scores(test_data))
