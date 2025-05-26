import json
import os

def merge_json_files(directory):
    merged_data = []
    for filename in os.listdir(directory):
        if filename.endswith(".json") and filename != "merged.json":
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    merged_data.extend(data)
            except Exception as e:
                print(f"⚠️ Skipping {file_path}: {e}")
    return merged_data

# Merge JSON files
merged_json = merge_json_files("knowledge_pool")

output_file_path = "knowledge_pool/merged.json"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(merged_json, output_file, indent=4, ensure_ascii=False)

print(f"✅ Merged JSON saved to {output_file_path}")
