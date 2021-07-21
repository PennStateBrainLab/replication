# Results Gathered With

zcat s2-corpus*.gz | jq -c '. | select(.paperAbstract,.title | test("(?i)(?:traumatic\\sbrain\\sinjury|concussion|neurotrauma|closed\\shead\\sinjury; i)"))'
