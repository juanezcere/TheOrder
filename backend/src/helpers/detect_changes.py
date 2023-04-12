def detect_changes(old_data, new_data):
    changes = []
    for field in old_data.keys():
        if field in new_data and new_data[field]:
            if new_data[field] != old_data[field]:
                changes.append(
                    {
                        'field': field,
                        'old_data': str(old_data[field]),
                        'new_data': str(new_data[field]),
                    }
                )
    return changes
