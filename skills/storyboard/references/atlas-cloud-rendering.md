# Optional Atlas Cloud Rendering

Use this path only after the six-frame narrative is approved and the user wants
actual image files. A written frame brief or a hand sketch remains the default and
the fallback.

## Protect the Story Before Rendering

1. Lock the persona, emotional arc, setting, and visual style across all six frames.
2. Reduce each frame to one visible action and one emotional beat.
3. Keep exact product UI, notifications, labels, and metrics out of generated pixels.
   Add required text in a layout tool after rendering.
4. Confirm the expected paid generation count with the user before submitting.

This preserves the storyboard's job: making the human journey discussable. More
polish does not compensate for a weak problem, forced solution, or unbelievable
outcome.

## Discover a Current Model

Confirm `ATLASCLOUD_API_KEY` is set without printing it. Read the live catalog and
the selected model's schema rather than relying on a remembered model name:

```bash
curl --fail-with-body https://api.atlascloud.ai/api/v1/models \
  -H "Authorization: Bearer $ATLASCLOUD_API_KEY" \
  -H "User-Agent: pm-storyboard-skill/1.0"
```

Choose a current text-to-image model that is enabled in the catalog. For example,
`google/nano-banana-2-lite/text-to-image-developer` supports `16:9` output when it
is present. Open the catalog entry's `schema` URL and verify the accepted fields
before building the request.

## Submit Each Approved Frame Once

Use one POST for one approved frame. Keep a stable character description and style
clause across the set, while changing only the frame's action, setting state, and
emotion.

```bash
curl --fail-with-body https://api.atlascloud.ai/api/v1/model/generateImage \
  -H "Authorization: Bearer $ATLASCLOUD_API_KEY" \
  -H "Content-Type: application/json" \
  -H "User-Agent: pm-storyboard-skill/1.0" \
  -d '{
    "model": "google/nano-banana-2-lite/text-to-image-developer",
    "prompt": "<persona + stable style + this frame's one action and emotion; no readable text or UI>",
    "aspect_ratio": "16:9",
    "resolution": "1k"
  }'
```

Do not automatically retry a generation POST. Save the returned prediction ID
immediately. If submission fails, deliver the frame brief or hand-sketch direction
instead of silently spending on another attempt.

## Poll, Inspect, and Record

Only poll the prediction returned by the successful POST, using bounded backoff:

```bash
curl --fail-with-body \
  -H "Authorization: Bearer $ATLASCLOUD_API_KEY" \
  -H "User-Agent: pm-storyboard-skill/1.0" \
  "https://api.atlascloud.ai/api/v1/model/prediction/<prediction-id>"
```

Stop on `completed`, `failed`, or the agreed timeout. Download completed outputs and
inspect every frame for persona drift, accidental text, invented product UI, missing
props, and an emotional beat that contradicts the narrative. Reject a polished image
that teaches the wrong story.

Keep a small manifest beside the rendered frames:

```json
{
  "frame": 1,
  "model": "google/nano-banana-2-lite/text-to-image-developer",
  "prediction_id": "<prediction-id>",
  "prompt": "<exact prompt>",
  "output": "frames/frame-01.png",
  "review": "accepted: persona, action, and emotion match the approved brief"
}
```

The manifest makes cost, provenance, and revisions visible. If a frame needs a new
generation, treat it as a new paid request and ask for approval again.
