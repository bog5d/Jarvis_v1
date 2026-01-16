import os
import re
import glob
from pathlib import Path
from collections import Counter
from datetime import datetime

class Gardener:
    def __init__(self):
        # Paths
        self.base_dir = Path("D:/My_System")
        self.log_dir = self.base_dir / "20_Knowledge_Base" / "Chat_Logs"
        self.report_dir = self.base_dir / "Jarvis_v1" / "reports"
        self.report_dir.mkdir(parents=True, exist_ok=True)
        
    def harvest(self):
        """Scan logs and harvest tags/insights"""
        print(f"🌱 Gardener starting harvest in {self.log_dir}...")
        
        all_tags = []
        insights = []
        total_dialogues = 0
        total_words = 0
        
        # Scan all .md files (Recursive or flat? Flat for Chat_Logs)
        files = list(self.log_dir.glob("*.md"))
        print(f"📄 Found {len(files)} log files.")
        
        # Regex for Tags
        # Format: 
        # **Tags**
        # * **Category**: ...
        # * **Keywords**: #tag1 #tag2
        tag_pattern = re.compile(r"\*\*Tags\*\*\s*\*\s*\*\*Category\*\*:\s*(.*?)\s*\*\s*\*\*Keywords\*\*:\s*(.*)", re.DOTALL | re.IGNORECASE)
        
        # Regex for User/Jarvis blocks to estimate words
        # ### HH:MM - Role
        
        for f in files:
            try:
                content = f.read_text(encoding='utf-8')
                total_words += len(content)
                
                # Split by interaction roughly (by "---")
                interactions = content.split("---")
                
                for block in interactions:
                    if not block.strip(): continue
                    total_dialogues += 1
                    
                    # Search for tags
                    match = tag_pattern.search(block)
                    if match:
                        category = match.group(1).strip()
                        keywords_str = match.group(2).strip()
                        
                        # Process Keywords
                        # Split by space or comma, usually #tag #tag
                        tags = [t.strip() for t in keywords_str.split() if t.startswith("#")]
                        all_tags.extend(tags)
                        
                        # Extract Summary (First ~100 chars of the block)
                        # Remove timestamps and roles for cleaner summary
                        clean_text = re.sub(r"### \d{2}:\d{2} - \w+", "", block).strip()
                        clean_text = clean_text.replace("**Tags**", "").split("\n")[0:2] # Take first 2 lines
                        summary = " ".join(clean_text)[:100] + "..."
                        
                        insights.append({
                            "category": category,
                            "tags": tags,
                            "summary": summary,
                            "file": f.name
                        })
            except Exception as e:
                print(f"❌ Error reading {f.name}: {e}")

        return {
            "tags_count": Counter(all_tags),
            "insights": insights,
            "stats": {
                "files": len(files),
                "dialogues": total_dialogues,
                "words": total_words
            }
        }

    def generate_report(self, data):
        """Generate Weekly Report Markdown"""
        today = datetime.now()
        week_num = today.strftime("%Y_%W")
        report_file = self.report_dir / f"Weekly_Report_{week_num}.md"
        
        top_tags = data["tags_count"].most_common(10)
        
        md = f"# 🌻 Weekly Garden Report ({week_num})\n\n"
        md += f"**Generated**: {today.strftime('%Y-%m-%d %H:%M')}\n\n"
        
        # 1. Vital Stats
        md += "## 📊 Vital Statistics\n"
        md += f"- **Conversations**: {data['stats']['dialogues']}\n"
        md += f"- **Words Processed**: {data['stats']['words']}\n"
        md += f"- **Active Tags**: {len(data['tags_count'])}\n\n"
        
        # 2. Trending Topics
        md += "## 🔥 Trending Topics (Top 10)\n"
        md += "| Tag | Frequency |\n|---|---|\n"
        for tag, count in top_tags:
            md += f"| {tag} | {count} |\n"
        md += "\n"
        
        # 3. Seedlings & Insights (Group by Category if possible, or list recent)
        md += "## 🌱 Seedlings (Recent Insights)\n"
        # Show last 5 insights
        for item in data["insights"][-10:]:
            tags_str = " ".join(item['tags'])
            md += f"> **{item['category']}**: {item['summary']}\n"
            md += f"> *Tags: {tags_str}* (from `{item['file']}`)\n\n"
            
        # Write to file
        with open(report_file, "w", encoding='utf-8') as f:
            f.write(md)
            
        print(f"✅ Report generated: {report_file}")
        return report_file

if __name__ == "__main__":
    gardener = Gardener()
    data = gardener.harvest()
    gardener.generate_report(data)
