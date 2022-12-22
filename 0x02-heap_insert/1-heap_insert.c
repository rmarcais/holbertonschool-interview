#include "binary_trees.h"

/**
 * left_depth - function that returns the depth of leftmost leaf
 * @tree: a pointer to the node to measure the depth
 * Return: The depth
 */
size_t left_depth(const binary_tree_t *tree)
{
	int d = 0;

	while (tree != NULL)
	{
		d++;
		tree = tree->left;
	}
	return (d);
}

/**
 * is_perfect - function that checks if a binary tree is perfect
 * @tree: a pointer to the node to measure the depth
 * @d: The depth
 * @level: The level of the leaves
 * Return: 0 or 1
 */
int is_perfect(const binary_tree_t *tree, int d, int level)
{
	if (tree == NULL)
		return (1);
	if (tree->left == NULL && tree->right == NULL)
	{
		if (d == level + 1)
			return (1);
		else
			return (0);
	}
	if (tree->left == NULL || tree->right == NULL)
		return (0);

	return (is_perfect(tree->left, d, level + 1) &&
		is_perfect(tree->right, d, level + 1));
}
/**
 * binary_tree_is_perfect - function that checks if a binary tree is perfect
 * @tree: a pointer to the node to measure the depth
 * Return: 0 or 1
 */
int binary_tree_is_perfect(const binary_tree_t *tree)
{
	int d = left_depth(tree);

	if (tree == NULL)
		return (0);
	return (is_perfect(tree, d, 0));
}

/**
 * count_nodes - Count the number of nodes in a binary tree
 * @tree: a pointer to the root node of the tree to check
 * Return: The number of nodes
 */
int count_nodes(const binary_tree_t *tree)
{
	if (tree == NULL)
		return (0);
	return (1 + count_nodes(tree->left) + count_nodes(tree->right));
}

/**
 * insert_complete_tree - Inserts a node in a complete tree
 * @root: a pointer to the root node of the tree
 * @value: Value to store in the node to be inserted
 * Return: The adress of the inserted node
 */
heap_t *insert_complete_tree(heap_t *root, int value)
{
	heap_t *tmp = root, *tmp_parent = root;
	bool left = false, right = false;

	while (tmp != NULL)
	{
		left = false;
		right = false;
		tmp_parent = tmp;
		if (count_nodes(tmp->left) == count_nodes(tmp->right))
		{
			left = true;
			tmp = tmp->left;
		}
		else if (binary_tree_is_perfect(tmp->left) == 0)
		{
			left = true;
			tmp = tmp->left;
		}
		else
		{
			right = true;
			tmp = tmp->right;
		}
	}
	if (left)
	{
		tmp_parent->left = binary_tree_node(tmp_parent, value);
		return (tmp_parent->left);
	}
	else if (right)
	{
		tmp_parent->right = binary_tree_node(tmp_parent, value);
		return (tmp_parent->right);
	}
	return (NULL);
}

/**
 * heap_insert - Inserts a value into a Max Binary Heap
 *
 * @root: Double pointer to the root node of the Heap
 * @value: Value to store in the node to be inserted
 *
 * Return: Pointer to the inserted node, or NULL on failure
 */
heap_t *heap_insert(heap_t **root, int value)
{
	heap_t *new;
	int tmp;

	if (*root == NULL)
	{
		new = binary_tree_node(NULL, value);
		*root = new;
	}
	else
	{
		new = insert_complete_tree(*root, value);
	}
	while (new->parent != NULL && new->n >= new->parent->n)
	{
		tmp = new->n;
		new->n = new->parent->n;
		new->parent->n = tmp;
		new = new->parent;
	}
	return (new);
}
