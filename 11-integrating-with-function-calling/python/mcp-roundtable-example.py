#!/usr/bin/env python3
"""
Model Context Protocol (MCP) Educational Example with Roundtable
================================================================

This example demonstrates how to use the Roundtable MCP Server for
educational purposes, building on the function calling concepts from
the main lesson.

Prerequisites:
- pip install roundtable-ai
- At least one supported AI assistant installed (claude, codex, etc.)

Learning Objectives:
- Understand how MCP extends function calling
- See unified AI assistant management in action
- Learn to compare different AI approaches
- Build educational workflows with multiple AI tools
"""

import subprocess
import json
import os
from typing import Dict, List, Optional

class EducationalMCPDemo:
    """
    Educational demonstration of MCP concepts using Roundtable AI
    """

    def __init__(self):
        self.available_assistants = []
        self.demo_questions = [
            {
                "question": "Explain what a REST API is",
                "category": "concept",
                "best_ai": "gemini"  # Good for explanations
            },
            {
                "question": "Create a simple Python function to calculate factorial",
                "category": "coding",
                "best_ai": "codex"  # Good for clean code
            },
            {
                "question": "Review this code for potential improvements",
                "category": "review",
                "best_ai": "claude"  # Good for code review
            },
            {
                "question": "Show me step-by-step how to debug this function",
                "category": "debugging",
                "best_ai": "cursor"  # Good for interactive help
            }
        ]

    def check_roundtable_installation(self) -> bool:
        """
        Check if Roundtable is properly installed
        """
        try:
            result = subprocess.run(
                ["roundtable-ai", "--help"],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False

    def discover_available_assistants(self) -> List[str]:
        """
        Discover which AI assistants are available through Roundtable

        This demonstrates the MCP concept of automatic tool discovery
        """
        try:
            result = subprocess.run(
                ["roundtable-ai", "--check"],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                # Parse the output to find available assistants
                output_lines = result.stdout.split('\n')
                available = []

                for line in output_lines:
                    if "✓" in line or "available" in line.lower():
                        # Extract assistant name (this is simplified parsing)
                        for assistant in ["claude", "codex", "gemini", "cursor"]:
                            if assistant in line.lower():
                                available.append(assistant)

                return list(set(available))  # Remove duplicates

        except subprocess.TimeoutExpired:
            print("⚠️  Discovery timeout - this is normal for first run")
        except FileNotFoundError:
            print("❌ Roundtable not found. Please install: pip install roundtable-ai")

        return []

    def demonstrate_mcp_concepts(self):
        """
        Educational demonstration of key MCP concepts
        """
        print("🎓 Model Context Protocol (MCP) Educational Demo")
        print("=" * 50)

        # 1. Installation Check
        print("\n1️⃣ Checking Roundtable Installation...")
        if not self.check_roundtable_installation():
            print("❌ Roundtable not installed")
            print("📋 Install with: pip install roundtable-ai")
            return
        print("✅ Roundtable is installed!")

        # 2. Tool Discovery (Core MCP Concept)
        print("\n2️⃣ Discovering Available AI Assistants...")
        self.available_assistants = self.discover_available_assistants()

        if not self.available_assistants:
            print("⚠️  No AI assistants detected")
            print("📋 Install at least one: claude, codex, gemini, or cursor")
            print("📋 Then run: roundtable-ai --check")
        else:
            print(f"✅ Found {len(self.available_assistants)} assistants:")
            for assistant in self.available_assistants:
                print(f"   • {assistant}")

        # 3. Educational Use Cases
        print("\n3️⃣ Educational Use Cases for MCP:")
        self.demonstrate_educational_scenarios()

        # 4. Practical Examples
        print("\n4️⃣ Practical Learning Examples:")
        self.show_learning_examples()

    def demonstrate_educational_scenarios(self):
        """
        Show different educational scenarios where MCP adds value
        """
        scenarios = {
            "Comparative Learning": {
                "description": "Compare how different AIs approach the same problem",
                "example": "Ask 'How do I sort a list?' to multiple AIs and compare approaches"
            },
            "Specialized Tasks": {
                "description": "Use the best AI for each type of learning task",
                "example": "Gemini for concepts, Codex for code, Claude for review"
            },
            "Workflow Integration": {
                "description": "Chain different AIs together for complex projects",
                "example": "Research → Code → Review → Deploy using different AIs"
            },
            "Context Sharing": {
                "description": "All AIs work with the same project context",
                "example": "Switch AIs mid-project without losing context"
            }
        }

        for scenario, details in scenarios.items():
            print(f"\n📚 {scenario}:")
            print(f"   • {details['description']}")
            print(f"   • Example: {details['example']}")

    def show_learning_examples(self):
        """
        Show practical examples students can try
        """
        for i, demo in enumerate(self.demo_questions, 1):
            print(f"\n🎯 Example {i}: {demo['category'].title()} Task")
            print(f"   Question: {demo['question']}")
            print(f"   Best AI for this: {demo['best_ai']}")
            print(f"   Why: {self.get_ai_strength(demo['best_ai'])}")

    def get_ai_strength(self, ai_name: str) -> str:
        """
        Educational explanation of each AI's strengths
        """
        strengths = {
            "claude": "Excellent for code review, explanations, and best practices",
            "codex": "Generates clean, professional code with good structure",
            "gemini": "Great for research, concepts, and detailed explanations",
            "cursor": "Interactive development and step-by-step guidance"
        }
        return strengths.get(ai_name, "General purpose AI assistant")

    def create_sample_mcp_config(self):
        """
        Generate sample MCP configuration for educational environments
        """
        configs = {
            "VS Code (Student IDE)": {
                "file_path": "~/.vscode/settings.json",
                "config": {
                    "mcp.servers": {
                        "roundtable-ai": {
                            "command": "roundtable-ai",
                            "env": {
                                "CLI_MCP_SUBAGENTS": "codex,claude,gemini,cursor",
                                "CLI_MCP_WORKING_DIR": "/path/to/student/project"
                            }
                        }
                    }
                }
            },
            "Claude Desktop (AI Learning)": {
                "file_path": "~/.config/claude_desktop_config.json",
                "config": {
                    "mcpServers": {
                        "roundtable-ai": {
                            "command": "roundtable-ai",
                            "env": {
                                "CLI_MCP_SUBAGENTS": "codex,claude,gemini,cursor"
                            }
                        }
                    }
                }
            }
        }

        print("\n📝 Sample MCP Configurations for Education:")
        print("=" * 45)

        for platform, details in configs.items():
            print(f"\n🔧 {platform}:")
            print(f"   File: {details['file_path']}")
            print(f"   Configuration:")
            print(json.dumps(details['config'], indent=6))

    def provide_next_steps(self):
        """
        Educational guidance for next steps
        """
        print("\n🚀 Next Steps in Your MCP Learning Journey:")
        print("=" * 45)

        steps = [
            "Install Roundtable: pip install roundtable-ai",
            "Check available tools: roundtable-ai --check",
            "Try the basic examples from this demo",
            "Set up MCP in your preferred IDE (VS Code, etc.)",
            "Experiment with different AI assistants for different tasks",
            "Build a learning project using multiple AIs",
            "Explore advanced MCP features and custom tools"
        ]

        for i, step in enumerate(steps, 1):
            print(f"{i}. {step}")

        print("\n📚 Additional Learning Resources:")
        print("• MCP Official Documentation: https://modelcontextprotocol.io")
        print("• Roundtable Repository: https://github.com/askbudi/roundtable")
        print("• Microsoft MCP for Beginners: https://github.com/microsoft/mcp-for-beginners")
        print("• Generative AI Learning Collection: https://aka.ms/genai-collection")

def main():
    """
    Main educational demonstration
    """
    demo = EducationalMCPDemo()

    print("🎓 Welcome to the MCP Educational Demo!")
    print("This demo shows how Model Context Protocol extends function calling")
    print("concepts to create unified AI assistant management for education.\n")

    # Run the full demonstration
    demo.demonstrate_mcp_concepts()
    demo.create_sample_mcp_config()
    demo.provide_next_steps()

    print("\n" + "=" * 60)
    print("🎉 Demo Complete! Ready to start your MCP learning journey?")
    print("💡 Try running: roundtable-ai --check")
    print("=" * 60)

if __name__ == "__main__":
    main()