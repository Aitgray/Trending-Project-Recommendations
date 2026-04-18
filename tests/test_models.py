import pytest
from pydantic import ValidationError

from src.models import ProjectIdea, TopicEntry, TopicSynthesis


def make_topic(slug: str) -> dict:
    return {
        "slug": slug,
        "title": slug.replace("-", " ").title(),
        "summary": f"Summary for {slug}",
        "supporting_repos": ["owner/repo1", "owner/repo2", "owner/repo3"],
    }


def make_project(slug: str, scope: str) -> dict:
    return {
        "title": f"{scope.title()} project for {slug}",
        "topic_slug": slug,
        "scope": scope,
        "pitch": "A two sentence pitch for this project.",
        "why_now": "Because it is trending right now.",
        "stack_hints": ["python", "fastapi"],
    }


def valid_synthesis(num_topics: int = 3, projects_per_topic: int = 1) -> dict:
    topics = [make_topic(f"topic-{i}") for i in range(num_topics)]
    projects = []
    for topic in topics:
        for scope in ["short", "medium", "long"]:
            for _ in range(projects_per_topic):
                projects.append(make_project(topic["slug"], scope))
    return {
        "week_of": "2024-01-21",
        "topics": topics,
        "whats_new": "Several new themes emerged this week.",
        "projects": projects,
    }


def test_valid_synthesis_3_topics():
    data = valid_synthesis(num_topics=3)
    synthesis = TopicSynthesis.model_validate(data)
    assert len(synthesis.topics) == 3
    assert len(synthesis.projects) == 9


def test_valid_synthesis_5_topics():
    data = valid_synthesis(num_topics=5)
    synthesis = TopicSynthesis.model_validate(data)
    assert len(synthesis.topics) == 5
    assert len(synthesis.projects) == 15


def test_too_few_topics():
    data = valid_synthesis(num_topics=2)
    with pytest.raises(ValidationError, match="topics must have 3-5 entries"):
        TopicSynthesis.model_validate(data)


def test_too_many_topics():
    data = valid_synthesis(num_topics=6)
    with pytest.raises(ValidationError, match="topics must have 3-5 entries"):
        TopicSynthesis.model_validate(data)


def test_too_few_projects():
    data = valid_synthesis(num_topics=3, projects_per_topic=1)
    # Remove two projects to get 7 (below minimum of 9)
    data["projects"] = data["projects"][:7]
    with pytest.raises(ValidationError, match="projects must have 9-15 entries"):
        TopicSynthesis.model_validate(data)


def test_too_many_projects():
    data = valid_synthesis(num_topics=3, projects_per_topic=2)
    # 3 topics * 3 scopes * 2 = 18 projects, above max of 15
    with pytest.raises(ValidationError, match="projects must have 9-15 entries"):
        TopicSynthesis.model_validate(data)


def test_invalid_scope():
    data = valid_synthesis(num_topics=3)
    data["projects"][0]["scope"] = "sprint"
    with pytest.raises(ValidationError):
        TopicSynthesis.model_validate(data)


def test_project_scopes():
    data = valid_synthesis(num_topics=3)
    synthesis = TopicSynthesis.model_validate(data)
    scopes = {p.scope for p in synthesis.projects}
    assert scopes == {"short", "medium", "long"}


def test_topic_slugs_are_strings():
    data = valid_synthesis(num_topics=3)
    synthesis = TopicSynthesis.model_validate(data)
    for topic in synthesis.topics:
        assert isinstance(topic.slug, str)
        assert len(topic.slug) > 0
